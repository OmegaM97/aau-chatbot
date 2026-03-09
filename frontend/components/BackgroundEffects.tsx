export default function BackgroundEffects() {
  const rippleConfigs = [
    // blue family
    { left: '8%',  top: '18%',  color: '#123164', delay: '0s',     size: 60 },
    { left: '22%', top: '62%',  color: '#233c5a', delay: '1.1s',   size: 72 },
    { left: '78%', top: '24%',  color: '#193664', delay: '3.4s',   size: 64 },

    // red family
    { left: '35%', top: '74%',  color: '#571818', delay: '0.7s',   size: 68 },
    { left: '88%', top: '48%',  color: '#532626', delay: '2.2s',   size: 56 },

    // purple family
    { left: '68%', top: '36%',  color: '#432263', delay: '1.8s',   size: 80 },
    { left: '14%', top: '84%',  color: '#47325c', delay: '4.1s',   size: 52 },
  ];

  return (
    <div className="fixed inset-0 z-0 overflow-hidden pointer-events-none">
      {/* Very subtle square grid – white lines on dark bg */}
      <div
        className="absolute inset-0"
        style={{
          backgroundImage: `
            linear-gradient(to right, rgba(255,255,255,0.09) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(255,255,255,0.09) 1px, transparent 1px)
          `,
          backgroundSize: '48px 48px',
          opacity: 0.7,           // ← tune this: 0.4–1.0
        }}
      />

      {/* Secondary finer grid (optional depth) */}
      <div
        className="absolute inset-0"
        style={{
          backgroundImage: `
            linear-gradient(to right, rgba(255,255,255,0.04) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(255,255,255,0.04) 1px, transparent 1px)
          `,
          backgroundSize: '96px 96px',
          opacity: 0.6,
        }}
      />

      {/* Water ripple layers – more visible + glowing */}
      {rippleConfigs.map((config, index) => (
        <div
          key={index}
          className="ripple"
          style={
            {
              left: config.left,
              top: config.top,
              width: `${config.size}px`,
              height: `${config.size}px`,
              '--ripple-color': config.color,
              animationDelay: config.delay,
            } as React.CSSProperties
          }
        />
      ))}
    </div>
  );
}