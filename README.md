# Pan-Tompkins-algorithm
Der Pan-Tompkins-Algorithmus ist ein weit verbreiteter Algorithmus zur QRS-Komplex-Detektion in Elektrokardiogrammen (EKGs). Er wurde von den Wissenschaftlern Pan und Tompkins entwickelt und ist bekannt für seine Effektivität bei der genauen Lokalisierung von QRS-Komplexen, die die elektrischen Aktivitäten des Herzens repräsentieren.

Der Algorithmus basiert auf der Analyse der Steigung (Slope), Amplitude und Dauer der EKG-Signale. Zunächst werden Tiefpass- und Hochpassfilter angewendet, um das Rauschen zu reduzieren und die relevanten Signale zu verstärken. Anschließend wird ein Ableitungsfilter verwendet, um die Steigung des Signals zu berechnen.

Um den QRS-Komplex zu identifizieren, wird eine adaptive Schwellenwertmethode angewendet, bei der die Amplitude des Signals basierend auf dem durchschnittlichen R-R-Intervall angepasst wird. Dies ermöglicht die Erkennung von QRS-Komplexen unabhängig von individuellen Variationen in der Signalamplitude.

Der Pan-Tompkins-Algorithmus zeichnet sich durch seine Robustheit gegenüber Störungen und seine Fähigkeit aus, R-Wellen zuverlässig zu erkennen, selbst bei schwierigen EKG-Signalen mit niedriger Qualität. Er wird häufig in EKG-Analysegeräten und medizinischen Überwachungssystemen eingesetzt, um eine schnelle und genaue Detektion von Herzaktivitäten zu ermöglichen.

Dank seiner einfachen Implementierung und guten Ergebnissen hat sich der Pan-Tompkins-Algorithmus als Standardmethode zur QRS-Komplex-Detektion etabliert und ist ein wichtiges Werkzeug für die Diagnose und Überwachung von Herzkrankheiten geworden.

##Ausgabe des eingegebnen Signals 
