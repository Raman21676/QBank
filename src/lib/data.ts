export interface Subject {
  code: string;
  name: string;
  slug: string;
  years: number[];
}

export interface Semester {
  number: number;
  name: string;
  slug: string;
  subjects: Subject[];
}

export const bcaSemesters: Semester[] = [
  {
    number: 1,
    name: "First Semester",
    slug: "semester-1",
    subjects: [
      { code: "CACS101", name: "Computer Fundamentals & Applications", slug: "computer-fundamentals", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS102", name: "Society & Technology", slug: "society-technology", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS103", name: "English I", slug: "english-i", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS104", name: "Mathematics I", slug: "mathematics-i", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS105", name: "Digital Logic", slug: "digital-logic", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
    ],
  },
  {
    number: 2,
    name: "Second Semester",
    slug: "semester-2",
    subjects: [
      { code: "CACS151", name: "C Programming", slug: "c-programming", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS152", name: "Financial Accounting", slug: "financial-accounting", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS153", name: "English II", slug: "english-ii", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS154", name: "Mathematics II", slug: "mathematics-ii", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS155", name: "Microprocessor & Computer Architecture", slug: "microprocessor-architecture", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
    ],
  },
  {
    number: 3,
    name: "Third Semester",
    slug: "semester-3",
    subjects: [
      { code: "CACS201", name: "Data Structures & Algorithms", slug: "data-structures-algorithms", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS202", name: "Probability & Statistics", slug: "probability-statistics", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS203", name: "System Analysis & Design", slug: "system-analysis-design", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS204", name: "OOP in Java", slug: "oop-java", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS205", name: "Web Technology", slug: "web-technology", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
    ],
  },
  {
    number: 4,
    name: "Fourth Semester",
    slug: "semester-4",
    subjects: [
      { code: "CACS251", name: "Operating Systems", slug: "operating-systems", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS252", name: "Numerical Methods", slug: "numerical-methods", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS253", name: "Software Engineering", slug: "software-engineering", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS254", name: "Scripting Language", slug: "scripting-language", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS255", name: "Database Management System", slug: "database-management-system", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
    ],
  },
  {
    number: 5,
    name: "Fifth Semester",
    slug: "semester-5",
    subjects: [
      { code: "CACS301", name: "MIS & E-Business", slug: "mis-ebusiness", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS302", name: "DotNet Technology", slug: "dotnet-technology", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS303", name: "Computer Networking", slug: "computer-networking", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS304", name: "Computer Graphics & Animation", slug: "computer-graphics", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS305", name: "Java Programming - II", slug: "java-programming-ii", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
    ],
  },
  {
    number: 6,
    name: "Sixth Semester",
    slug: "semester-6",
    subjects: [
      { code: "CACS351", name: "Network Programming", slug: "network-programming", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS352", name: "Mobile Programming", slug: "mobile-programming", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS353", name: "Distributed Systems", slug: "distributed-systems", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS354", name: "Applied Economics", slug: "applied-economics", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS355", name: "Project II", slug: "project-ii", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
    ],
  },
  {
    number: 7,
    name: "Seventh Semester",
    slug: "semester-7",
    subjects: [
      { code: "CACS401", name: "Advanced Java Programming", slug: "advanced-java", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS402", name: "Data Warehousing & Data Mining", slug: "data-warehousing-mining", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS403", name: "Cloud Computing", slug: "cloud-computing", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS404", name: "Cyber Law", slug: "cyber-law", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
    ],
  },
  {
    number: 8,
    name: "Eighth Semester",
    slug: "semester-8",
    subjects: [
      { code: "CACS451", name: "Project Work", slug: "project-work", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
      { code: "CACS452", name: "Internship", slug: "internship", years: [2018, 2019, 2020, 2021, 2022, 2023, 2024] },
    ],
  },
];

export function getSemesterBySlug(slug: string): Semester | undefined {
  return bcaSemesters.find((s) => s.slug === slug);
}

export function getSubjectBySlug(semesterSlug: string, subjectSlug: string): Subject | undefined {
  const sem = getSemesterBySlug(semesterSlug);
  return sem?.subjects.find((s) => s.slug === subjectSlug);
}

export function getAllSemesterSlugs(): string[] {
  return bcaSemesters.map((s) => s.slug);
}

export function getAllSubjectPaths(): { semester: string; subject: string }[] {
  const paths: { semester: string; subject: string }[] = [];
  for (const sem of bcaSemesters) {
    for (const sub of sem.subjects) {
      paths.push({ semester: sem.slug, subject: sub.slug });
    }
  }
  return paths;
}

export function getAllYearPaths(): { semester: string; subject: string; year: string }[] {
  const paths: { semester: string; subject: string; year: string }[] = [];
  for (const sem of bcaSemesters) {
    for (const sub of sem.subjects) {
      for (const year of sub.years) {
        paths.push({ semester: sem.slug, subject: sub.slug, year: String(year) });
      }
    }
  }
  return paths;
}
