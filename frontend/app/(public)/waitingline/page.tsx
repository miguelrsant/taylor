"use client";

import { useState } from "react";
import confetti from "canvas-confetti";

export default function Page() {
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    setMessage("");

    const form = e.currentTarget;
    const name = (form.elements.namedItem("name") as HTMLInputElement).value;
    const email = (form.elements.namedItem("email") as HTMLInputElement).value;

    try {
      const res = await fetch(`/api/waitingline/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ name, email }),
      });

      if (!res.ok) {
        throw new Error("Erro ao cadastrar");
      }

      confetti({
        particleCount: 250,
        spread: 80,
        origin: { y: 0.6 },
      });

      setMessage(
        "🎉 Seu cadastro foi confirmado! Em breve você receberá novidades especiais.",
      );

      form.reset();
    } catch {
      setMessage("❌ Algo deu errado. Tente novamente em instantes.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="waitingline">
      <div className="card-waitingline">
        <h1 className="waiting-taylor text-gradient">TAYLOR</h1>

        <p>
          Cadastre seu e-mail para receber novidades e atualizações da
          plataforma enquanto estamos em desenvolvimento.
        </p>

        <div className="cadastro-taylor">
          <form onSubmit={handleSubmit}>
            <input type="text" name="name" placeholder="Joãozinho" required />
            <input
              type="email"
              name="email"
              placeholder="joaozinho@email.com"
              required
            />

            <button
              type="submit"
              disabled={loading}
              style={{ cursor: "pointer" }}
            >
              {loading ? "Cadastrando..." : "Cadastrar"}
            </button>
          </form>

          {message && (
            <p
              className="status-message"
              style={{
                marginTop: "12px",
                fontWeight: 600,
                textAlign: "center",
              }}
            >
              {message}
            </p>
          )}

          <p className="p-footer">
            Designed & Developed by{" "}
            <strong>
              <a
                className="text-gradient"
                href="https://www.linkedin.com/in/miguelrsant/"
              >
                Miguel Angelo
              </a>
            </strong>
          </p>
        </div>
      </div>
    </div>
  );
}
