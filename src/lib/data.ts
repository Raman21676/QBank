import bcaManifest from "@/content/bca.json";
import baManifest from "@/content/ba.json";
import bitManifest from "@/content/bit.json";

// Types
export interface Paper {
  year: number;
  hasQuestions: boolean;
  hasAnswers: boolean;
  questionSize?: string;
  answerSize?: string;
  pages?: number;
  fm?: number;
  pm?: number;
  duration?: string;
}

export interface Subject {
  code: string;
  name: string;
  slug: string;
  papers: Paper[];
}

export interface Semester {
  number: number;
  name: string;
  slug: string;
  subjects: Subject[];
}

export interface FacultyManifest {
  id: string;
  name: string;
  shortName: string;
  slug: string;
  icon: string;
  description: string;
  totalSemesters: number;
  color: string;
  bgGlow: string;
  semesters: Semester[];
}

// Faculty registry
export const faculties: FacultyManifest[] = [bcaManifest, baManifest, bitManifest];

// Individual exports for convenience
export const bcaData = bcaManifest;
export const baData = baManifest;
export const bitData = bitManifest;

// Helper functions
export function getFacultyBySlug(slug: string): FacultyManifest | undefined {
  return faculties.find((f) => f.slug === slug);
}

export function getSemesterBySlug(facultySlug: string, semesterSlug: string): Semester | undefined {
  const faculty = getFacultyBySlug(facultySlug);
  return faculty?.semesters.find((s) => s.slug === semesterSlug);
}

export function getSubjectBySlug(
  facultySlug: string,
  semesterSlug: string,
  subjectSlug: string
): Subject | undefined {
  const semester = getSemesterBySlug(facultySlug, semesterSlug);
  return semester?.subjects.find((s) => s.slug === subjectSlug);
}

export function getPaperByYear(
  facultySlug: string,
  semesterSlug: string,
  subjectSlug: string,
  year: number
): Paper | undefined {
  const subject = getSubjectBySlug(facultySlug, semesterSlug, subjectSlug);
  return subject?.papers.find((p) => p.year === year);
}

// Static path generators for Next.js
export function getAllFacultySlugs(): string[] {
  return faculties.map((f) => f.slug);
}

export function getAllSemesterPaths(): { faculty: string; semester: string }[] {
  const paths: { faculty: string; semester: string }[] = [];
  for (const faculty of faculties) {
    for (const sem of faculty.semesters) {
      paths.push({ faculty: faculty.slug, semester: sem.slug });
    }
  }
  return paths;
}

export function getAllSubjectPaths(): { faculty: string; semester: string; subject: string }[] {
  const paths: { faculty: string; semester: string; subject: string }[] = [];
  for (const faculty of faculties) {
    for (const sem of faculty.semesters) {
      for (const sub of sem.subjects) {
        paths.push({ faculty: faculty.slug, semester: sem.slug, subject: sub.slug });
      }
    }
  }
  return paths;
}

export function getAllYearPaths(): {
  faculty: string;
  semester: string;
  subject: string;
  year: string;
}[] {
  const paths: { faculty: string; semester: string; subject: string; year: string }[] = [];
  for (const faculty of faculties) {
    for (const sem of faculty.semesters) {
      for (const sub of sem.subjects) {
        for (const paper of sub.papers) {
          paths.push({
            faculty: faculty.slug,
            semester: sem.slug,
            subject: sub.slug,
            year: String(paper.year),
          });
        }
      }
    }
  }
  return paths;
}

// Stats helpers
export function getTotalPaperCount(): number {
  let count = 0;
  for (const faculty of faculties) {
    for (const sem of faculty.semesters) {
      for (const sub of sem.subjects) {
        count += sub.papers.length;
      }
    }
  }
  return count;
}

export function getAvailablePaperCount(): number {
  let count = 0;
  for (const faculty of faculties) {
    for (const sem of faculty.semesters) {
      for (const sub of sem.subjects) {
        count += sub.papers.filter((p) => p.hasQuestions).length;
      }
    }
  }
  return count;
}

export function getSubjectCount(facultySlug: string): number {
  const faculty = getFacultyBySlug(facultySlug);
  if (!faculty) return 0;
  return faculty.semesters.reduce((acc, sem) => acc + sem.subjects.length, 0);
}

// Search index generation
export interface SearchItem {
  id: string;
  type: "faculty" | "semester" | "subject" | "paper";
  title: string;
  subtitle: string;
  faculty: string;
  facultySlug: string;
  semester?: string;
  semesterSlug?: string;
  subject?: string;
  subjectSlug?: string;
  subjectCode?: string;
  year?: number;
  href: string;
}

export function generateSearchIndex(): SearchItem[] {
  const items: SearchItem[] = [];

  for (const faculty of faculties) {
    // Faculty item
    items.push({
      id: `${faculty.slug}-faculty`,
      type: "faculty",
      title: faculty.shortName,
      subtitle: faculty.name,
      faculty: faculty.name,
      facultySlug: faculty.slug,
      href: `/${faculty.slug}/`,
    });

    for (const sem of faculty.semesters) {
      // Semester item
      items.push({
        id: `${faculty.slug}-${sem.slug}-semester`,
        type: "semester",
        title: `${faculty.shortName} — ${sem.name}`,
        subtitle: `${sem.subjects.length} subjects`,
        faculty: faculty.name,
        facultySlug: faculty.slug,
        semester: sem.name,
        semesterSlug: sem.slug,
        href: `/${faculty.slug}/${sem.slug}/`,
      });

      for (const sub of sem.subjects) {
        // Subject item
        items.push({
          id: `${faculty.slug}-${sem.slug}-${sub.slug}-subject`,
          type: "subject",
          title: sub.name,
          subtitle: `${faculty.shortName} · ${sem.name} · ${sub.code}`,
          faculty: faculty.name,
          facultySlug: faculty.slug,
          semester: sem.name,
          semesterSlug: sem.slug,
          subject: sub.name,
          subjectSlug: sub.slug,
          subjectCode: sub.code,
          href: `/${faculty.slug}/${sem.slug}/${sub.slug}/`,
        });

        for (const paper of sub.papers) {
          // Paper item
          items.push({
            id: `${faculty.slug}-${sem.slug}-${sub.slug}-${paper.year}-paper`,
            type: "paper",
            title: `${sub.name} ${paper.year}`,
            subtitle: `${faculty.shortName} · ${sem.name} · ${paper.year}`,
            faculty: faculty.name,
            facultySlug: faculty.slug,
            semester: sem.name,
            semesterSlug: sem.slug,
            subject: sub.name,
            subjectSlug: sub.slug,
            subjectCode: sub.code,
            year: paper.year,
            href: `/${faculty.slug}/${sem.slug}/${sub.slug}/${paper.year}/`,
          });
        }
      }
    }
  }

  return items;
}

// Simple fuzzy search
export function searchItems(query: string, items: SearchItem[]): SearchItem[] {
  if (!query.trim()) return [];
  
  const normalizedQuery = query.toLowerCase().trim();
  const terms = normalizedQuery.split(/\s+/);
  
  return items
    .map((item) => {
      const text = `${item.title} ${item.subtitle} ${item.subjectCode || ""}`.toLowerCase();
      let score = 0;
      
      for (const term of terms) {
        if (text.includes(term)) {
          score += 1;
          // Boost exact matches in title
          if (item.title.toLowerCase().includes(term)) score += 2;
          if (item.subjectCode?.toLowerCase().includes(term)) score += 3;
        }
      }
      
      return { item, score };
    })
    .filter(({ score }) => score > 0)
    .sort((a, b) => b.score - a.score)
    .map(({ item }) => item)
    .slice(0, 10);
}
