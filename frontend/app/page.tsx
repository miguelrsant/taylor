"use client";

import Home from "@/components/Home/HomePage";
import Pilares from "@/components/Home/SectionPilares";
import Escolher from "@/components/Home/SectionEscolher";
import Impulsionam from "@/components/Home/SectionImpulcionam";
import Negocio from "@/components/Home/SectionNegocio";
import Logind from "@/components/Assets/Loding";
import { useLayoutEffect } from "react";

export default function HomePage() {
  useLayoutEffect(() => {
    requestAnimationFrame(() => {
      window.scrollTo(0, 0);
      setTimeout(() => window.scrollTo(0, 0), 50);
    });
  }, []);

  return (
    <div className="all-content">
      <Logind></Logind>
      <Home></Home>
      <Pilares></Pilares>
      <Escolher></Escolher>
      <Impulsionam></Impulsionam>
      <Negocio></Negocio>
    </div>
  );
}
