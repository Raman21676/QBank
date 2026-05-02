"use client";

import { motion } from "framer-motion";
import { BookOpen, GraduationCap, FileText, Download, ArrowRight } from "lucide-react";
import Link from "next/link";
import { FacultyCard } from "@/components/FacultyCard";
import { StatsSection } from "@/components/StatsSection";

const faculties = [
  {
    id: "bca",
    name: "BCA",
    fullName: "Bachelor of Computer Applications",
    description: "8 semesters of programming, algorithms, databases, web tech, and more.",
    icon: BookOpen,
    color: "from-sky-400 to-sky-500",
    bgGlow: "bg-sky-100/50",
    semesters: 8,
    papers: 120,
    href: "/bca/",
  },
  {
    id: "ba",
    name: "BA",
    fullName: "Bachelor of Arts",
    description: "Humanities and social sciences — English, Economics, Political Science, History, and more.",
    icon: GraduationCap,
    color: "from-leaf-400 to-leaf-500",
    bgGlow: "bg-leaf-100/50",
    semesters: 4,
    papers: 80,
    href: "/ba/",
  },
  {
    id: "bit",
    name: "BIT",
    fullName: "Bachelor of Information Technology",
    description: "Core IT skills, networking, cybersecurity, cloud computing, and software engineering.",
    icon: FileText,
    color: "from-teal-400 to-teal-500",
    bgGlow: "bg-teal-100/50",
    semesters: 8,
    papers: 100,
    href: "/bit/",
  },
];

export default function HomePage() {
  return (
    <div className="relative overflow-hidden">
      {/* Decorative blobs */}
      <div className="absolute top-0 left-0 w-[500px] h-[500px] bg-sky-200/30 rounded-full blur-3xl -translate-x-1/2 -translate-y-1/2" />
      <div className="absolute top-40 right-0 w-[400px] h-[400px] bg-leaf-200/30 rounded-full blur-3xl translate-x-1/3" />

      {/* Hero Section */}
      <section className="relative pt-32 pb-20 md:pt-40 md:pb-28 px-6">
        <div className="mx-auto max-w-5xl text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
          >
            <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-sky-50 border border-sky-100 text-sky-600 text-xs font-semibold uppercase tracking-wider mb-6">
              <span className="w-2 h-2 rounded-full bg-sky-500 animate-pulse" />
              Free for all TU students
            </div>
          </motion.div>

          <motion.h1
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.1 }}
            className="text-4xl md:text-6xl lg:text-7xl font-extrabold text-slate-900 leading-tight tracking-tight"
          >
            Your Complete{" "}
            <span className="text-gradient">TU Question</span>
            <br className="hidden md:block" /> Bank Archive
          </motion.h1>

          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="mt-6 text-lg md:text-xl text-slate-500 max-w-2xl mx-auto leading-relaxed"
          >
            Download past exam papers and comprehensive answer sheets for
            Tribhuvan University programs. Organized by faculty, semester, and
            year.
          </motion.p>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.3 }}
            className="mt-10 flex flex-col sm:flex-row items-center justify-center gap-4"
          >
            <Link
              href="/bca/"
              className="group inline-flex items-center gap-2 px-8 py-4 rounded-2xl bg-gradient-to-r from-sky-500 to-sky-400 text-white font-semibold shadow-lg shadow-sky-200/50 hover:shadow-sky-300/60 hover:-translate-y-0.5 transition-all duration-200"
            >
              Explore BCA Papers
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </Link>
            <Link
              href="#faculties"
              className="inline-flex items-center gap-2 px-8 py-4 rounded-2xl bg-white text-slate-700 font-semibold border border-slate-200 shadow-sm hover:bg-slate-50 hover:-translate-y-0.5 transition-all duration-200"
            >
              View All Faculties
            </Link>
          </motion.div>
        </div>
      </section>

      {/* Stats */}
      <StatsSection />

      {/* Faculties Section */}
      <section id="faculties" className="relative py-20 px-6">
        <div className="mx-auto max-w-6xl">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-16"
          >
            <h2 className="text-3xl md:text-4xl font-bold text-slate-900">
              Choose Your <span className="text-gradient">Faculty</span>
            </h2>
            <p className="mt-4 text-slate-500 max-w-lg mx-auto">
              Select your program to browse past questions organized by semester
              and subject.
            </p>
          </motion.div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8">
            {faculties.map((faculty, index) => (
              <FacultyCard key={faculty.id} faculty={faculty} index={index} />
            ))}
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="relative py-20 px-6 bg-white/40">
        <div className="mx-auto max-w-5xl">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-16"
          >
            <h2 className="text-3xl md:text-4xl font-bold text-slate-900">
              How It <span className="text-gradient">Works</span>
            </h2>
          </motion.div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {[
              {
                step: "01",
                title: "Select Your Paper",
                desc: "Browse by faculty, semester, subject, and year to find the exact paper you need.",
                icon: BookOpen,
              },
              {
                step: "02",
                title: "Download Questions",
                desc: "Get the clean, reformatted question paper PDF ready for printing or digital study.",
                icon: Download,
              },
              {
                step: "03",
                title: "Get Answers Too",
                desc: "Each paper comes with a comprehensive answer sheet including diagrams and code.",
                icon: FileText,
              },
            ].map((item, index) => (
              <motion.div
                key={item.step}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1 }}
                className="relative text-center p-8 rounded-3xl bg-white/70 border border-slate-100 shadow-sm"
              >
                <div className="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br from-sky-400 to-leaf-400 text-white mb-6">
                  <item.icon className="w-6 h-6" />
                </div>
                <span className="absolute top-6 right-6 text-5xl font-extrabold text-slate-100 select-none">
                  {item.step}
                </span>
                <h3 className="text-lg font-bold text-slate-800 mb-3">
                  {item.title}
                </h3>
                <p className="text-sm text-slate-500 leading-relaxed">
                  {item.desc}
                </p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
}
