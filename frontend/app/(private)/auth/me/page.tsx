import { cookies } from "next/headers";
import ButtonLogout from "@/components/Buttons/ButtonLogout";
export const dynamic = "force-dynamic";

export default async function Page() {
  const cookieStore = await cookies();
  const token = cookieStore.get("token")?.value;

  const res = await fetch(`${process.env.API_URL}/me`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    cache: "no-store",
  });

  const contentType = res.headers.get("content-type") || "";
  const body = contentType.includes("application/json")
    ? await res.json()
    : await res.text();

  return (
    <div className="PageMe">
      <h1>Status: {res.status}</h1>
      <pre>{JSON.stringify(body, null, 2)}</pre>
      <ButtonLogout />
    </div>
  );
}
