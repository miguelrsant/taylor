import Home from '@/components/home-page/home'
import Pilares from '@/components/home-page/pilares';
import Escolher from '@/components/home-page/escolher';
import Impulsionam from '@/components/home-page/impulsionam';
import Negocio from '@/components/home-page/negocio';


export default function HomePage() {
  return (
    <div className="all-content">
      <Home></Home>
      <Pilares></Pilares>
      <Escolher></Escolher>
      <Impulsionam></Impulsionam>
      <Negocio></Negocio>
    </div>
    
  );
}
