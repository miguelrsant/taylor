"use client"

import { gsap } from 'gsap';
import { useEffect } from 'react';
import { ScrollTrigger } from "gsap/ScrollTrigger";


export default function Negocio() {
          useEffect(() => {
          gsap.registerPlugin(ScrollTrigger)
          gsap.fromTo(
              ".cartao-negocio",
              { y: 100,
                opacity: 0
              },
              {
              y: 0,
              opacity: 1,
              duration: 1,
              scrollTrigger: {
                trigger: '.cartao-negocio',
              }
              }
          );
          gsap.fromTo(
              ".text-cartao-negocio",
              { y: 50,
                opacity: 0
              },
              {
              y: 0,
              opacity: 1,
              duration: 1,
              scrollTrigger: {
                trigger: ".cartao-negocio",
              }
              }
          );
          gsap.fromTo(
              ".btn-negocio",
              { y: 50,
                opacity: 0
              },
              {
              y: 0,
              opacity: 1,
              duration: 1,
              scrollTrigger: {
                trigger: ".cartao-negocio",
              }
              }
          );
          gsap.fromTo(
              ".p-footer",
              { y: 100,
                opacity: 0
              },
              {
              y: 0,
              opacity: 1,
              duration: .5,
              scrollTrigger: {
                trigger: '.footer-negocio',
              }
              }
          );
          }, []);
    return (
              <div className="negocio">
        <div className="gradiente-negocio">
          <div className="cartao-negocio">
            <div className="text-cartao-negocio">
              <h1>Pronto para transformar <strong  className="text-gradient">seu negócio?</strong></h1>
              <p>Junte-se às empresas que já automatizam processos, geram indights e tomam decisões mais inteligentes com TAYLOR.</p>
            </div>
            <div className="btns-negocio">
               <a  className="btn-negocio" href="/waitingline" style={{textDecoration: "none"}} ><div className="btn-comecar"><p>Começar agora →</p></div></a>
            </div>
          </div>
        </div>
        <footer className="footer-negocio">
            <p className='p-footer'>Designed & Developed by <strong><a className='text-gradient' href="https://www.linkedin.com/in/miguelrsant/">Miguel Angelo</a></strong></p>
            <p  className='p-footer'>© 2025 TAYLOR — Todos os direitos reservados.</p>
        </footer>
      </div>
    )
}