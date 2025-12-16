import { NextResponse } from "next/server";
import { cookies } from "next/headers";

export async function POST() {
  const cookieStore = await cookies();
  const token = cookieStore.get("token")?.value;

  if (!token) {
    return NextResponse.json({ msg: "Token não encontrado" }, { status: 401 });
  }
  await fetch(`${process.env.API_URL}/logout`, {
    method: "POST",
    headers: {
      "content-type": "application/json",
    },
    body: JSON.stringify({ session_token: token }),
  });

  cookieStore.set("token", "", {
    maxAge: 0,
    path: "/",
  });

  return NextResponse.json({ msg: "Logout realizado" });
}
