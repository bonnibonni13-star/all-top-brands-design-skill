# Lizenzen und Herkunft

## Magic UI

Die Effektnamen in `KATALOG.md` und die Installationszeilen unter `React:` verweisen auf **Magic UI**:

- https://github.com/magicuidesign/magicui
- MIT-Lizenz, © Magic UI
- Installation in React-/Next.js-Projekten mit Tailwind: `npx shadcn@latest add @magicui/<name>`

Magic UI ist eine React-Bibliothek. In einem React-Projekt lohnt es sich, die fertigen Komponenten zu nehmen statt sie nachzubauen.

## Was hier eigene Arbeit ist

In diesem Ordner wird **kein Quelltext von Magic UI weitergegeben**. Eigene Arbeit dieses Skills sind:

- die Beschreibungen, Dosierungs- und Wertangaben in `KATALOG.md`,
- die Hinweise unter `Web:`, `Compose:` und `Barrierefreiheit:`,
- sämtliche Umsetzungen in `animationen.html` (reines CSS und JavaScript, ohne fremde Bibliotheken),
- die Zuordnung der Effekte zu den Ansätzen des Skills.

Die Einträge decken außerdem Bewegungen ab, die es bei Magic UI gar nicht gibt, weil sie zu Apps statt zu Websites gehören: gestaffeltes Einblenden, Druck-Zustand, gemeinsame Elemente, Skelett-Laden, Ziehen zum Aktualisieren, Fokus auf dem Fernseher, Blatt von unten und Meldung von unten.

## Sonstiges

`animationen.html` lädt nichts aus dem Netz: keine Schriften, keine Bibliotheken, keine Bilder. Das Rauschmuster entsteht aus einem eingebetteten SVG-Filter.
