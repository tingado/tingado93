using Toybox.Application;
using Toybox.WatchUi;
import Toybox.Lang;

// Punto de entrada de la app.
class GymApp extends Application.AppBase {

    public function initialize() {
        AppBase.initialize();
    }

    // Primera pantalla: menú para elegir la sesión.
    public function getInitialView() as Array<WatchUi.Views or WatchUi.InputDelegates> {
        var sessions = SampleData.sessions();

        var menu = new WatchUi.Menu2({:title => WatchUi.loadResource(Rez.Strings.ChooseSession)});
        for (var i = 0; i < sessions.size(); i++) {
            menu.addItem(new WatchUi.MenuItem(
                sessions[i].name,
                sessions[i].subtitle(),
                i,               // id = índice de la sesión
                null
            ));
        }

        return [menu, new SessionMenuDelegate(sessions)];
    }
}
