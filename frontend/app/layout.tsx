import type { Metadata } from "next";

import '../public/styles/index.css' 

const metadata: Metadata = {
  title: "Taylor: Business Super Intelligence Platform",
  description: "TAYLOR é uma plataforma avançada de automação operacional e análise inteligente, transformando dados em decisões estratégicas para empresas de todos os setores.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {

  return (
    <html lang="pt-br"
    data-lt-installed="true">
      <head>
        <link rel="shortcut icon" href="./svg/taylor-logo-white.svg"/>
      </head>
      <body>
        {children}
      </body>
    </html>
  );
}