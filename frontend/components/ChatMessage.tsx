'use client';

import { useEffect, useState } from "react";
import type { Message } from '@/types/chat';

interface ChatMessageProps {
  message: Message;
}

export default function ChatMessage({ message }: ChatMessageProps) {
  const isUser = message.role === 'user';
  const [displayedText, setDisplayedText] = useState(isUser ? message.content : '');

  useEffect(() => {
    if (isUser) {
      setDisplayedText(message.content);
      return;
    }

    // Reset displayed text when message changes
    setDisplayedText('');
    let index = 0;
    
    const interval = setInterval(() => {
      if (index < message.content.length) {
        setDisplayedText(message.content.substring(0, index + 1));
        index++;
      } else {
        clearInterval(interval);
      }
    }, 25);

    return () => clearInterval(interval);
  }, [message.content, isUser]);

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} group`}>
      <div
        className={`max-w-[78%] px-5 py-4 rounded-3xl leading-relaxed shadow-sm transition-all text-[18px] md:text-[18px] font-mono ${
          isUser
            ? 'bg-white/10 text-zinc-200 rounded-tr-none' // semi-transparent gray bg
            : 'text-zinc-100 rounded-tl-none' // bot: no bg
        }`}
      >
        {displayedText}
        {!isUser && displayedText.length < message.content.length && (
          <span className="animate-pulse">|</span>
        )}
      </div>
    </div>
  );
}