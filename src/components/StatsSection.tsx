"use client";

import { motion } from "framer-motion";
import { FileText, Download, BookOpen, Layers } from "lucide-react";
import { faculties, getTotalPaperCount } from "@/lib/data";

export function StatsSection() {
  const totalSemesters = faculties.reduce((acc, f) => acc + f.totalSemesters, 0);
  const totalPapers = getTotalPaperCount();
  const totalSubjects = faculties.reduce(
    (acc, f) => acc + f.semesters.reduce((sacc, s) => sacc + s.subjects.length, 0),
    0
  );

  const stats = [
    { icon: BookOpen, value: String(faculties.length), label: "Faculties" },
    { icon: Layers, value: String(totalSemesters), label: "Semesters" },
    { icon: FileText, value: String(totalSubjects), label: "Subjects" },
    { icon: Download, value: String(totalPapers), label: "Paper Slots" },
  ];

  return (
    <section className="relative py-12 px-6">
      <div className="mx-auto max-w-5xl">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {stats.map((stat, index) => (
            <motion.div
              key={stat.label}
              initial={{ opacity: 0, scale: 0.9 }}
              whileInView={{ opacity: 1, scale: 1 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.1 }}
              className="flex flex-col items-center p-6 rounded-2xl bg-white/60 border border-slate-100 shadow-sm"
            >
              <stat.icon className="w-6 h-6 text-sky-500 mb-3" />
              <span className="text-2xl md:text-3xl font-extrabold text-slate-800">
                {stat.value}
              </span>
              <span className="text-xs text-slate-400 font-medium mt-1">
                {stat.label}
              </span>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
