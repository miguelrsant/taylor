import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function middleware(req: NextRequest) {
  const token = req.cookies.get("token")?.value;
  const { pathname } = req.nextUrl;

  const isAuthRoute =
    pathname.startsWith("/signin") || pathname.startsWith("/register");

  const isProtectedRoute =
    pathname.startsWith("/auth/me") ||
    pathname.startsWith("/status") ||
    pathname.startsWith("/auth/logout");

  if (token && isAuthRoute) {
    return NextResponse.redirect(new URL("/", req.url));
  }

  if (!token && isProtectedRoute) {
    return NextResponse.redirect(new URL("/signin", req.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/((?!_next|favicon.ico|.*\\.(?:png|jpg|jpeg|gif|svg|webp)).*)"],
};
