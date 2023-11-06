def command_help(command="help"):
    
    match (command):
        case "help-slash":
            return "Dieser Befehl. Zeigt Hilfe für den angegebenen Befehl.\nSyntax: /help befehl:(BEFEHL)\n\nNutze '/help commands' um eine Liste aller Befehle zu erhalten."
        case "help":
            return "Dieser Befehl. Zeigt Hilfe für den angegebenen Befehl.\nSyntax: %help (BEFEHL)\n\nNutze 'help commands' um eine Liste aller Befehle zu erhalten."
        case "setlogs":
            return 'Setzt den Channel in dem Befehle gelogt werden. Entfernt den LogChannel falls die Aktion "Entfernen" ist. Channel als ID angeben. Admin only.'
        case "database":
            return "Der Befehl um direkt mit der Datenbank zu interagieren. Nur für den Entwickler."
        case "reminder":
            return "Nutze diesen Befehl um den Bot dich an etwas erinnern zu lassen. Syntax: /reminder erinnerung: (NACHRICHT) stunden: x(optional) minuten: x(optional) sekunden: x(optional)"
        case "commandtoggle":
            return "Schaltet Befehle ein oder aus. Nur für den Entwickler."
        case "soe":
            return "Nur ein kleiner Test Befehl"
        case "farbrolle":
            return "Gibt dem Nutzer eine Farbrolle oder bearbeitet sie. Die Farbe kann mit oder ohne # genannt werden und ist als Hex Code einzugeben. Der Standard ist Weiß. \nSyntax: %farbrolle (FARBE)"
        case "commands":

            returnText = "Hier ist eine Liste aller Befehle:\n"
            for command in commands:
                returnText += "{}\n".format(command)
            return returnText
        
        case _:
            return "Unbekannter Befehl"

commands = ( "help-slash", "help", "setlogs", "database", "reminder", "commandtoggle", "soe", "farbrolle", "farbrolle-slash")