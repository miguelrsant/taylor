import { NextResponse } from "next/server";

export async function POST(req: Request) {
  try {
    const body = await req.json();

    const backendRes = await fetch(`${process.env.API_URL}/singin/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),

      credentials: "include",
      cache: "no-store",
    });

    const setCookie = backendRes.headers.get("set-cookie");
    const data = await backendRes.json();

    const response = NextResponse.json(data, {
      status: backendRes.status,
    });

    if (setCookie) {
      response.headers.append("set-cookie", setCookie);
    }

    return response;
  } catch (error) {
    return NextResponse.json(
      { status: "error", message: "Erro ao conectar ao servidor." },
      { status: 500 }
    );
  }
}
