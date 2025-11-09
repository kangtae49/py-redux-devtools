import {useEffect} from "react";
import { Root } from '@redux-devtools/app';
import "./App.css"
function App() {
  useEffect(() => {

    const handleKeyDown = (e: KeyboardEvent) => {
      const isRefreshKey =
        (e.key === 'F5') ||
        (e.key === 'r' && (e.ctrlKey || e.metaKey));

      if (isRefreshKey) {
        e.preventDefault();
        window.location.reload()
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);
  return (
    <Root />
  )
}

export default App
