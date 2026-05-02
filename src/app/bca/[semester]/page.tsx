import { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft, ArrowRight, FileText } from "lucide-react";
import { getSemesterBySlug, bcaSemesters } from "@/lib/data";
import { SemesterPageClient } from "@/components/SemesterPageClient";

export function generateStaticParams() {
  return bcaSemesters.map((s) => ({ semester: s.slug }));
}

export function generateMetadata({ params }: { params: { semester: string } }): Metadata {
  const semester = getSemesterBySlug(params.semester);
  return {
    title: semester ? `${semester.name} — BCA | TU QBank` : "Not Found",
  };
}

export default function SemesterPage({
  params,
}: {
  params: { semester: string };
}) {
  const semester = getSemesterBySlug(params.semester);
  if (!semester) return notFound();

  return (
    <div className="relative pt-28 pb-20 px-6">
      <div className="mx-auto max-w-5xl">
        <SemesterPageClient semester={semester} />
      </div>
    </div>
  );
}
