"use client";

import { motion } from "framer-motion";
import Link from "next/link";
import {
  ArrowLeft,
  ArrowRight,
  Calendar,
  Download,
  FileText,
  CheckCircle,
} from "lucide-react";
import type { Semester, Subject } from "@/lib/data";

export function SubjectPageClient({
  semester,
  subject,
}: {
  semester: Semester;
  subject: Subject;
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
          href={`/bca/${semester.slug}/`}
          className="inline-flex items-center gap-1 text-sm text-slate-400 hover:text-sky-600 transition-colors"
        >
          <ArrowLeft className="w-4 h-4" />
          Back to {semester.name}
        </Link>
      </motion.div>

      {/* Header */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="mb-10 p-6 rounded-2xl bg-white/80 border border-slate-100 shadow-sm"
      >
        <div className="flex items-start gap-4">
          <div className="flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br from-sky-400 to-sky-500 text-white shadow-md shrink-0">
            <FileText className="w-7 h-7" />
          </div>
          <div>
            <p className="text-xs font-mono text-sky-500 font-medium uppercase tracking-wider">
              {subject.code}
            </p>
            <h1 className="text-2xl md:text-3xl font-extrabold text-slate-900 mt-1">
              {subject.name}
            </h1>
            <p className="text-sm text-slate-500 mt-2">
              {semester.name} &middot; {subject.years.length} years available
            </p>
          </div>
        </div>
      </motion.div>

      {/* Year List */}
      <div className="space-y-4">
        {subject.years.map((year, index) => (
          <motion.div
            key={year}
            initial={{ opacity: 0, y: 15 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: index * 0.05 }}
          >
            <Link
              href={`/bca/${semester.slug}/${subject.slug}/${year}/`}
              className="group flex items-center justify-between p-5 rounded-2xl bg-white/80 border border-slate-100 shadow-sm hover:shadow-md hover:border-sky-100 transition-all duration-200"
            >
              <div className="flex items-center gap-4">
                <div className="flex items-center justify-center w-11 h-11 rounded-xl bg-leaf-50 text-leaf-500 group-hover:bg-leaf-100 transition-colors">
                  <Calendar className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-base font-semibold text-slate-800 group-hover:text-sky-700 transition-colors">
                    {year} Question Paper
                  </h3>
                  <div className="flex items-center gap-3 mt-1.5">
                    <span className="inline-flex items-center gap-1 text-xs text-slate-400">
                      <FileText className="w-3 h-3" />
                      Questions
                    </span>
                    <span className="inline-flex items-center gap-1 text-xs text-slate-400">
                      <CheckCircle className="w-3 h-3" />
                      Answers
                    </span>
                  </div>
                </div>
              </div>
              <div className="flex items-center gap-2">
                <span className="hidden sm:inline-flex items-center gap-1 text-xs font-medium text-sky-600 bg-sky-50 px-3 py-1.5 rounded-lg group-hover:bg-sky-100 transition-colors">
                  <Download className="w-3.5 h-3.5" />
                  Download
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
