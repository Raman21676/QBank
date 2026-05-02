"use client";

import { motion } from "framer-motion";
import Link from "next/link";
import { ArrowRight, BookOpen, GraduationCap, FileText } from "lucide-react";
import type { FacultyManifest } from "@/lib/data";
import { getSubjectCount } from "@/lib/data";

const iconMap: Record<string, React.ComponentType<{ className?: string }>> = {
  BookOpen,
  GraduationCap,
  FileText,
};

export function FacultyCard({
  faculty,
  index,
}: {
  faculty: FacultyManifest;
  index: number;
}) {
  const Icon = iconMap[faculty.icon] || BookOpen;
  const subjectCount = getSubjectCount(faculty.slug);
  const paperCount = faculty.semesters.reduce(
    (acc, sem) => acc + sem.subjects.reduce((sacc, sub) => sacc + sub.papers.length, 0),
    0
  );

  return (
    <motion.div
      initial={{ opacity: 0, y: 30 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true }}
      transition={{ delay: index * 0.1, duration: 0.5 }}
    >
      <Link
        href={`/${faculty.slug}/`}
        className="group relative block h-full"
      >
        <div
          className={`absolute inset-0 rounded-3xl ${faculty.bgGlow} opacity-0 group-hover:opacity-100 transition-opacity duration-300 blur-xl`}
        />
        <div className="relative h-full p-7 rounded-3xl bg-white/80 border border-slate-100 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300">
          <div
            className={`inline-flex items-center justify-center w-12 h-12 rounded-2xl bg-gradient-to-br ${faculty.color} text-white shadow-lg mb-5`}
          >
            <Icon className="w-6 h-6" />
          </div>

          <h3 className="text-2xl font-bold text-slate-800 mb-1">
            {faculty.shortName}
          </h3>
          <p className="text-xs text-slate-400 font-medium uppercase tracking-wider mb-4">
            {faculty.name}
          </p>
          <p className="text-sm text-slate-500 leading-relaxed mb-6">
            {faculty.description}
          </p>

          <div className="flex items-center justify-between pt-4 border-t border-slate-100">
            <div className="flex items-center gap-4 text-xs text-slate-400">
              <span>{faculty.totalSemesters} Semesters</span>
              <span>{paperCount} Papers</span>
            </div>
            <div className="flex items-center gap-1 text-sm font-semibold text-sky-600 group-hover:text-sky-700 transition-colors">
              Browse
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </div>
          </div>
        </div>
      </Link>
    </motion.div>
  );
}
