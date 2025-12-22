"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

export default function ButtonLogout() {
  const router = useRouter();
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (loading) return;
    setLoading(true);

    try {
      const res = await fetch("/api/logout", {
        method: "POST",
        cache: "no-store",
      });

      if (!res.ok) {
        throw new Error("Logout failed");
      }

      router.replace("/singin");
    } catch (err) {
      console.error(err);
      alert("Erro ao sair. Tente novamente.");
      setLoading(false);
    }
  };

  return (
    <div className="">
      <form onSubmit={handleSubmit}>
        <button
          type="submit"
          disabled={loading}
          style={{ cursor: loading ? "not-allowed" : "pointer" }}
        >
          {loading ? "Saindo..." : "Logout"}
        </button>
      </form>
    </div>
  );
}
