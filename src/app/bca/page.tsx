"use client";

import { motion } from "framer-motion";
import Link from "next/link";
import { BookOpen, ArrowRight, Layers } from "lucide-react";
import { bcaSemesters } from "@/lib/data";

export default function BCAPage() {
  return (
    <div className="relative pt-28 pb-20 px-6">
      <div className="mx-auto max-w-6xl">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center mb-16"
        >
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-sky-50 border border-sky-100 text-sky-600 text-xs font-semibold uppercase tracking-wider mb-6">
            <BookOpen className="w-3.5 h-3.5" />
            Bachelor of Computer Applications
          </div>
          <h1 className="text-3xl md:text-5xl font-extrabold text-slate-900">
            BCA <span className="text-gradient">Question Papers</span>
          </h1>
          <p className="mt-4 text-slate-500 max-w-xl mx-auto">
            Browse past exam papers and answer sheets for all 8 semesters of TU
            BCA program.
          </p>
        </motion.div>

        {/* Semester Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
          {bcaSemesters.map((semester, index) => (
            <motion.div
              key={semester.slug}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.05 }}
            >
              <Link
                href={`/bca/${semester.slug}/`}
                className="group block h-full"
              >
                <div className="h-full p-6 rounded-2xl bg-white/80 border border-slate-100 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300">
                  <div className="flex items-center justify-between mb-4">
                    <div className="flex items-center justify-center w-12 h-12 rounded-xl bg-gradient-to-br from-sky-400 to-sky-500 text-white shadow-md">
                      <Layers className="w-6 h-6" />
                    </div>
                    <span className="text-3xl font-extrabold text-slate-100 group-hover:text-sky-100 transition-colors">
                      {semester.number}
                    </span>
                  </div>
                  <h3 className="text-lg font-bold text-slate-800 mb-1">
                    {semester.name}
                  </h3>
                  <p className="text-sm text-slate-400 mb-4">
                    {semester.subjects.length} Subjects
                  </p>
                  <div className="flex items-center gap-1 text-sm font-medium text-sky-600 group-hover:text-sky-700">
                    View Subjects
                    <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                  </div>
                </div>
              </Link>
            </motion.div>
          ))}
        </div>
      </div>
    </div>
  );
}
