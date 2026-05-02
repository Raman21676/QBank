import { Metadata } from "next";
import { notFound } from "next/navigation";
import {
  getSubjectBySlug,
  getSemesterBySlug,
  bcaSemesters,
} from "@/lib/data";
import { YearPageClient } from "@/components/YearPageClient";

export function generateStaticParams() {
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

export function generateMetadata({
  params,
}: {
  params: { semester: string; subject: string; year: string };
}): Metadata {
  const subject = getSubjectBySlug(params.semester, params.subject);
  return {
    title: subject
      ? `${subject.name} ${params.year} — BCA | TU QBank`
      : "Not Found",
  };
}

export default function YearPage({
  params,
}: {
  params: { semester: string; subject: string; year: string };
}) {
  const semester = getSemesterBySlug(params.semester);
  const subject = getSubjectBySlug(params.semester, params.subject);
  const year = parseInt(params.year);

  if (!semester || !subject || isNaN(year) || !subject.years.includes(year)) {
    return notFound();
  }

  return (
    <div className="relative pt-28 pb-20 px-6">
      <div className="mx-auto max-w-3xl">
        <YearPageClient semester={semester} subject={subject} year={year} />
      </div>
    </div>
  );
}
