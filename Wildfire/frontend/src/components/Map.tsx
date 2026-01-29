import React, { useRef, useEffect } from 'react';
import maplibregl from 'maplibre-gl';
import 'maplibre-gl/dist/maplibre-gl.css';

const Map: React.FC = () => {
  const mapContainer = useRef<HTMLDivElement>(null);
  const map = useRef<maplibregl.Map | null>(null);

  useEffect(() => {
    if (map.current) return;
    if (mapContainer.current) {
        map.current = new maplibregl.Map({
        container: mapContainer.current,
        style: 'https://demotiles.maplibre.org/style.json',
        center: [0, 0],
        zoom: 2
      });
    }
    
    return () => {
        map.current?.remove();
        map.current = null;
    }
  }, []);

  return (
    <div className="relative w-full h-screen">
      <div ref={mapContainer} className="absolute inset-0" />
      <div className="absolute top-4 left-4 bg-white p-4 rounded shadow-lg z-10">
        <h1 className="text-xl font-bold">Wildfire Monitor</h1>
        <p className="text-sm text-gray-500">MVP Status: Active</p>
      </div>
    </div>
  );
};

export default Map;
