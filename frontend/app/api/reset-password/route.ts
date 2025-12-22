import { NextResponse } from "next/server";

export async function POST(req: Request) {
  try {
    const body = await req.json();

    const backendRes = await fetch(`${process.env.API_URL}/reset/`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${body.token}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ new_password: body.new_password }),
    });

    const data = await backendRes.json();

    const response = NextResponse.json(data, {
      status: backendRes.status,
    });

    return response;
  } catch (error) {
    return NextResponse.json(
      { status: "error", message: "Erro ao conectar ao servidor." },
      { status: 500 }
    );
  }
}
