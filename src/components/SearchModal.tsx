"use client";

import { useState, useEffect, useCallback, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Search, X, FileText, BookOpen, GraduationCap, Calendar, Layers } from "lucide-react";
import Link from "next/link";
import { generateSearchIndex, searchItems, type SearchItem } from "@/lib/data";

const searchIndex = generateSearchIndex();

function getItemIcon(type: SearchItem["type"]) {
  switch (type) {
    case "faculty":
      return BookOpen;
    case "semester":
      return Layers;
    case "subject":
      return GraduationCap;
    case "paper":
      return Calendar;
    default:
      return FileText;
  }
}

function getItemColor(type: SearchItem["type"]) {
  switch (type) {
    case "faculty":
      return "bg-sky-50 text-sky-500";
    case "semester":
      return "bg-leaf-50 text-leaf-500";
    case "subject":
      return "bg-amber-50 text-amber-500";
    case "paper":
      return "bg-violet-50 text-violet-500";
    default:
      return "bg-slate-50 text-slate-500";
  }
}

export function SearchModal({ isOpen, onClose }: { isOpen: boolean; onClose: () => void }) {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<SearchItem[]>([]);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (isOpen) {
      setTimeout(() => inputRef.current?.focus(), 100);
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "";
      setQuery("");
      setResults([]);
    }
    return () => {
      document.body.style.overflow = "";
    };
  }, [isOpen]);

  const handleSearch = useCallback((value: string) => {
    setQuery(value);
    setResults(searchItems(value, searchIndex));
  }, []);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "k" && (e.metaKey || e.ctrlKey)) {
        e.preventDefault();
        isOpen ? onClose() : onClose();
      }
      if (e.key === "Escape" && isOpen) {
        onClose();
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [isOpen, onClose]);

  return (
    <AnimatePresence>
      {isOpen && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.15 }}
          className="fixed inset-0 z-50 flex items-start justify-center pt-[15vh] px-4"
          onClick={onClose}
        >
          {/* Backdrop */}
          <div className="absolute inset-0 bg-slate-900/40 backdrop-blur-sm" />

          {/* Modal */}
          <motion.div
            initial={{ opacity: 0, y: -20, scale: 0.95 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: -20, scale: 0.95 }}
            transition={{ duration: 0.2 }}
            className="relative w-full max-w-2xl bg-white rounded-3xl shadow-2xl overflow-hidden"
            onClick={(e) => e.stopPropagation()}
          >
            {/* Search Input */}
            <div className="flex items-center gap-3 px-6 py-5 border-b border-slate-100">
              <Search className="w-5 h-5 text-slate-400 shrink-0" />
              <input
                ref={inputRef}
                type="text"
                value={query}
                onChange={(e) => handleSearch(e.target.value)}
                placeholder="Search subjects, papers, or faculties..."
                className="flex-1 bg-transparent text-slate-800 placeholder:text-slate-400 text-base outline-none"
              />
              <button
                onClick={onClose}
                className="flex items-center gap-1 text-xs text-slate-400 bg-slate-100 px-2 py-1 rounded-lg hover:bg-slate-200 transition-colors"
              >
                <span className="hidden sm:inline">ESC</span>
                <X className="w-3.5 h-3.5 sm:hidden" />
              </button>
            </div>

            {/* Results */}
            <div className="max-h-[50vh] overflow-y-auto">
              {query.trim() === "" ? (
                <div className="px-6 py-8 text-center">
                  <p className="text-sm text-slate-400">
                    Type to search across all faculties, semesters, subjects, and papers.
                  </p>
                  <div className="mt-4 flex flex-wrap justify-center gap-2">
                    {["BCA", "Data Structures", "OOP Java", "2020"].map((term) => (
                      <button
                        key={term}
                        onClick={() => handleSearch(term)}
                        className="px-3 py-1.5 rounded-full bg-slate-50 text-slate-500 text-xs font-medium hover:bg-sky-50 hover:text-sky-600 transition-colors"
                      >
                        {term}
                      </button>
                    ))}
                  </div>
                </div>
              ) : results.length === 0 ? (
                <div className="px-6 py-12 text-center">
                  <FileText className="w-10 h-10 text-slate-200 mx-auto mb-3" />
                  <p className="text-sm text-slate-400">No results found for &quot;{query}&quot;</p>
                </div>
              ) : (
                <div className="py-2">
                  {results.map((item, index) => {
                    const Icon = getItemIcon(item.type);
                    return (
                      <Link
                        key={item.id}
                        href={item.href}
                        onClick={onClose}
                        className="flex items-center gap-4 px-6 py-3 hover:bg-slate-50 transition-colors group"
                      >
                        <div
                          className={`flex items-center justify-center w-10 h-10 rounded-xl ${getItemColor(
                            item.type
                          )} shrink-0`}
                        >
                          <Icon className="w-4 h-4" />
                        </div>
                        <div className="flex-1 min-w-0">
                          <h4 className="text-sm font-semibold text-slate-800 group-hover:text-sky-600 transition-colors truncate">
                            {item.title}
                          </h4>
                          <p className="text-xs text-slate-400 truncate">{item.subtitle}</p>
                        </div>
                        <span className="text-xs font-medium text-slate-300 capitalize shrink-0">
                          {item.type}
                        </span>
                      </Link>
                    );
                  })}
                </div>
              )}
            </div>

            {/* Footer */}
            <div className="px-6 py-3 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
              <span className="text-xs text-slate-400">
                {results.length > 0 ? `${results.length} results` : `${searchIndex.length} items indexed`}
              </span>
              <span className="text-xs text-slate-400">
                Press <kbd className="px-1.5 py-0.5 bg-white rounded text-slate-500 border border-slate-200">Enter</kbd> to select
              </span>
            </div>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
