export default function Header() {
  return (
    <header>
      <nav>
        <ul>
          <li>
            <a href="/signin">Signin</a>
          </li>
          <li>
            <a href="/register">Register</a>
          </li>
          <li>
            <a href="/auth/me">Me</a>
          </li>
        </ul>
      </nav>
    </header>
  );
}
