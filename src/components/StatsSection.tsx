"use client";

import { motion } from "framer-motion";
import { FileText, Download, BookOpen, Users } from "lucide-react";

const stats = [
  { icon: BookOpen, value: "3", label: "Faculties" },
  { icon: FileText, value: "300+", label: "Question Papers" },
  { icon: Download, value: "600+", label: "PDF Downloads" },
  { icon: Users, value: "20+", label: "Subjects Covered" },
];

export function StatsSection() {
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
