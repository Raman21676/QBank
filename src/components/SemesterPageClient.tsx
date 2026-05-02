"use client";

import { motion } from "framer-motion";
import Link from "next/link";
import { ArrowLeft, ArrowRight, FileText } from "lucide-react";
import type { FacultyManifest, Semester } from "@/lib/data";

export function SemesterPageClient({
  faculty,
  semester,
}: {
  faculty: FacultyManifest;
  semester: Semester;
}) {
  return (
    <>
      {/* Breadcrumb */}
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        className="mb-8"
      >
        <Link
          href={`/${faculty.slug}/`}
          className="inline-flex items-center gap-1 text-sm text-slate-400 hover:text-sky-600 transition-colors"
        >
          <ArrowLeft className="w-4 h-4" />
          Back to {faculty.shortName}
        </Link>
      </motion.div>

      {/* Header */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="mb-12"
      >
        <h1 className="text-3xl md:text-4xl font-extrabold text-slate-900">
          {semester.name}{" "}
          <span className="text-gradient">Subjects</span>
        </h1>
        <p className="mt-3 text-slate-500">
          Select a subject to view past question papers and answer sheets.
        </p>
      </motion.div>

      {/* Subjects */}
      <div className="space-y-4">
        {semester.subjects.map((subject, index) => (
          <motion.div
            key={subject.slug}
            initial={{ opacity: 0, x: -20 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ delay: index * 0.05 }}
          >
            <Link
              href={`/${faculty.slug}/${semester.slug}/${subject.slug}/`}
              className="group flex items-center justify-between p-5 rounded-2xl bg-white/80 border border-slate-100 shadow-sm hover:shadow-md hover:border-sky-100 transition-all duration-200"
            >
              <div className="flex items-center gap-4">
                <div className="flex items-center justify-center w-11 h-11 rounded-xl bg-sky-50 text-sky-500 group-hover:bg-sky-100 transition-colors">
                  <FileText className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-base font-semibold text-slate-800 group-hover:text-sky-700 transition-colors">
                    {subject.name}
                  </h3>
                  <p className="text-xs text-slate-400 font-mono mt-0.5">
                    {subject.code}
                  </p>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <span className="hidden sm:inline-flex items-center gap-1 text-xs text-slate-400 bg-slate-50 px-2.5 py-1 rounded-lg">
                  {subject.papers.length} Years
                </span>
                <ArrowRight className="w-5 h-5 text-slate-300 group-hover:text-sky-500 group-hover:translate-x-1 transition-all" />
              </div>
            </Link>
          </motion.div>
        ))}
      </div>
    </>
  );
}
