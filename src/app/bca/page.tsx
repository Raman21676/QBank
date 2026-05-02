import { Metadata } from "next";
import { bcaData } from "@/lib/data";
import { FacultyPageClient } from "@/components/FacultyPageClient";

export const metadata: Metadata = {
  title: "BCA — Bachelor of Computer Applications | TU QBank",
  description:
    "Browse past exam papers and answer sheets for all 8 semesters of TU BCA program.",
};

export default function BCAPage() {
  return <FacultyPageClient faculty={bcaData} />;
}
