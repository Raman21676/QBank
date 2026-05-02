import { Metadata } from "next";
import { notFound } from "next/navigation";
import { baData, getSemesterBySlug } from "@/lib/data";
import { SemesterPageClient } from "@/components/SemesterPageClient";

export function generateStaticParams() {
  return baData.semesters.map((s) => ({ semester: s.slug }));
}

export function generateMetadata({ params }: { params: { semester: string } }): Metadata {
  const semester = getSemesterBySlug("ba", params.semester);
  return {
    title: semester ? `${semester.name} — BA | TU QBank` : "Not Found",
  };
}

export default function SemesterPage({
  params,
}: {
  params: { semester: string };
}) {
  const semester = getSemesterBySlug("ba", params.semester);
  if (!semester) return notFound();

  return (
    <div className="relative pt-28 pb-20 px-6">
      <div className="mx-auto max-w-5xl">
        <SemesterPageClient faculty={baData} semester={semester} />
      </div>
    </div>
  );
}
