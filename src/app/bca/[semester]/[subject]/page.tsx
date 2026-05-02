import { Metadata } from "next";
import { notFound } from "next/navigation";
import {
  getSubjectBySlug,
  getSemesterBySlug,
  bcaSemesters,
} from "@/lib/data";
import { SubjectPageClient } from "@/components/SubjectPageClient";

export function generateStaticParams() {
  const paths: { semester: string; subject: string }[] = [];
  for (const sem of bcaSemesters) {
    for (const sub of sem.subjects) {
      paths.push({ semester: sem.slug, subject: sub.slug });
    }
  }
  return paths;
}

export function generateMetadata({
  params,
}: {
  params: { semester: string; subject: string };
}): Metadata {
  const semester = getSemesterBySlug(params.semester);
  const subject = getSubjectBySlug(params.semester, params.subject);
  return {
    title: subject
      ? `${subject.name} — ${semester?.name} BCA | TU QBank`
      : "Not Found",
  };
}

export default function SubjectPage({
  params,
}: {
  params: { semester: string; subject: string };
}) {
  const semester = getSemesterBySlug(params.semester);
  const subject = getSubjectBySlug(params.semester, params.subject);
  if (!semester || !subject) return notFound();

  return (
    <div className="relative pt-28 pb-20 px-6">
      <div className="mx-auto max-w-4xl">
        <SubjectPageClient semester={semester} subject={subject} />
      </div>
    </div>
  );
}
