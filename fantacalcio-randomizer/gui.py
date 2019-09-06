import fantacalcio_randomizer
from appJar import gui

# handle button events


def press(button):
    if button == "Cancel":
        app.stop()
    else:
        filename = app.getEntry("Quotazioni")
        n_teams = app.getEntry("Quante squadre? ")
        teams_names = []
        for i in range(int(n_teams)):
            teams_names.append(app.getEntry("Nome squadra " + str(i+1)))

        fantacalcio_randomizer.draw_teams(filename, int(n_teams), teams_names)
        app.infoBox("Squadre create!",
                    "Puoi trovare le squadre in formato .txt nella cartella")


def add_teams_names_entries(n_teams_entry):
    for i in range(int(app.getEntry(n_teams_entry))):
        app.addLabelEntry("Nome squadra " + str(i+1))

    # link the buttons to the function called press
    app.addButtons(["Submit", "Cancel"], press)


# create a GUI variable called app
app = gui("Fantacalcio Randomizer", "400x200")
app.setFont(18)
app.setLocation("CENTER")
app.setGuiPadding(4, 4)

# add & configure widgets - widgets get a name, to help referencing them later
app.addFileEntry("Quotazioni")
app.setEntryDefault("Quotazioni", "Aggiungere il file excel delle quotazioni")

app.addLabelEntry("Quante squadre? ")
app.setEntrySubmitFunction("Quante squadre? ", add_teams_names_entries)
app.setEntryDefault("Quante squadre? ", "ex: 8")

# start the GUI
app.go()
