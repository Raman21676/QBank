import { Metadata } from "next";
import { notFound } from "next/navigation";
import { baData, getSubjectBySlug } from "@/lib/data";
import { SubjectPageClient } from "@/components/SubjectPageClient";

export function generateStaticParams() {
  const paths: { semester: string; subject: string }[] = [];
  for (const sem of baData.semesters) {
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
  const subject = getSubjectBySlug("ba", params.semester, params.subject);
  return {
    title: subject ? `${subject.name} — BA | TU QBank` : "Not Found",
  };
}

export default function SubjectPage({
  params,
}: {
  params: { semester: string; subject: string };
}) {
  const semester = baData.semesters.find((s) => s.slug === params.semester);
  const subject = getSubjectBySlug("ba", params.semester, params.subject);
  if (!semester || !subject) return notFound();

  return (
    <div className="relative pt-28 pb-20 px-6">
      <div className="mx-auto max-w-5xl">
        <SubjectPageClient faculty={baData} semester={semester} subject={subject} />
      </div>
    </div>
  );
}
