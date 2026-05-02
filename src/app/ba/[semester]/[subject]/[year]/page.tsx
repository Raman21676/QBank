import { Metadata } from "next";
import { notFound } from "next/navigation";
import { baData, getSubjectBySlug, getPaperByYear } from "@/lib/data";
import { YearPageClient } from "@/components/YearPageClient";

export function generateStaticParams() {
  const paths: { semester: string; subject: string; year: string }[] = [];
  for (const sem of baData.semesters) {
    for (const sub of sem.subjects) {
      for (const paper of sub.papers) {
        paths.push({ semester: sem.slug, subject: sub.slug, year: String(paper.year) });
      }
    }
  }
  return paths;
}

export function generateMetadata({
  params,
}: {
  params: { semester: string; subject: string; year: string };
}): Metadata {
  const subject = getSubjectBySlug("ba", params.semester, params.subject);
  return {
    title: subject
      ? `${subject.name} ${params.year} — BA | TU QBank`
      : "Not Found",
  };
}

export default function YearPage({
  params,
}: {
  params: { semester: string; subject: string; year: string };
}) {
  const semester = baData.semesters.find((s) => s.slug === params.semester);
  const subject = getSubjectBySlug("ba", params.semester, params.subject);
  const paper = getPaperByYear("ba", params.semester, params.subject, Number(params.year));
  if (!semester || !subject || !paper) return notFound();

  return (
    <div className="relative pt-28 pb-20 px-6">
      <div className="mx-auto max-w-5xl">
        <YearPageClient faculty={baData} semester={semester} subject={subject} paper={paper} />
      </div>
    </div>
  );
}
