import { Metadata } from "next";
import { notFound } from "next/navigation";
import { bitData, getSubjectBySlug } from "@/lib/data";
import { SubjectPageClient } from "@/components/SubjectPageClient";

export function generateStaticParams() {
  const paths: { semester: string; subject: string }[] = [];
  for (const sem of bitData.semesters) {
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
  const subject = getSubjectBySlug("bit", params.semester, params.subject);
  return {
    title: subject ? `${subject.name} — BIT | TU QBank` : "Not Found",
  };
}

export default function SubjectPage({
  params,
}: {
  params: { semester: string; subject: string };
}) {
  const semester = bitData.semesters.find((s) => s.slug === params.semester);
  const subject = getSubjectBySlug("bit", params.semester, params.subject);
  if (!semester || !subject) return notFound();

  return (
    <div className="relative pt-28 pb-20 px-6">
      <div className="mx-auto max-w-5xl">
        <SubjectPageClient faculty={bitData} semester={semester} subject={subject} />
      </div>
    </div>
  );
}
