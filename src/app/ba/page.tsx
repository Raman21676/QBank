import { Metadata } from "next";
import { baData } from "@/lib/data";
import { FacultyPageClient } from "@/components/FacultyPageClient";

export const metadata: Metadata = {
  title: "BA — Bachelor of Arts | TU QBank",
  description:
    "Browse past exam papers and answer sheets for all 4 semesters of TU BA program.",
};

export default function BAPage() {
  return <FacultyPageClient faculty={baData} />;
}
