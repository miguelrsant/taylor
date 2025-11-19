"use server"

export default async function Page() {
  const host = process.env.NEXT_API
  const res = await fetch(`${host}/status/`, { cache: "no-store" });

  if (!res.ok) throw new Error(`Erro: ${res.statusText}`);

  const body = await res.json();

  return (
    <div>
      <h1>Resposta do Backend</h1>
      <pre>{JSON.stringify(body, null, 2)}</pre>
    </div>
  );
}
