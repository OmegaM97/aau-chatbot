import BackgroundEffects from '@/components/BackgroundEffects';
import ChatContainer from '@/components/ChatContainer';

export default function Home() {
  return (
    <div className="relative min-h-screen overflow-hidden">
      <BackgroundEffects />
      <ChatContainer />
    </div>
  );
}