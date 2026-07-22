using Toybox.WatchUi;
using Toybox.Graphics;
using Toybox.Timer;
import Toybox.Lang;

// Cuenta regresiva del descanso entre series. Grande y centrada.
// Al llegar a 0 vibra y vuelve sola a la vista de ejercicio.
class RestView extends WatchUi.View {
    private var _m as SessionManager;
    private var _remaining as Number;
    private var _timer as Timer.Timer or Null;
    private var _finished as Boolean;

    public function initialize(manager as SessionManager, seconds as Number) {
        View.initialize();
        _m = manager;
        _remaining = seconds;
        _timer = null;
        _finished = false;
    }

    public function onShow() as Void {
        _timer = new Timer.Timer();
        _timer.start(method(:onTick), 1000, true);
    }

    public function onHide() as Void {
        if (_timer != null) {
            _timer.stop();
            _timer = null;
        }
    }

    public function onTick() as Void {
        _remaining--;
        if (_remaining <= 0 && !_finished) {
            _finished = true;
            Feedback.restOver();
            WatchUi.requestUpdate();
            // Volvemos a la vista de ejercicio (ya apunta a la nueva serie).
            WatchUi.popView(WatchUi.SLIDE_RIGHT);
            return;
        }
        WatchUi.requestUpdate();
    }

    public function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        var cx = w / 2;

        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_BLACK);
        dc.clear();

        // Etiqueta "DESCANSO".
        dc.setColor(Graphics.COLOR_BLUE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(cx, h * 0.22, Graphics.FONT_SMALL, "DESCANSO", Graphics.TEXT_JUSTIFY_CENTER);

        // Segundos restantes (número grande).
        var secs = (_remaining > 0) ? _remaining : 0;
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(cx, h * 0.42, Graphics.FONT_NUMBER_THAI_HOT, secs.toString(), Graphics.TEXT_JUSTIFY_CENTER);

        // Próximo: nombre + serie que viene.
        dc.setColor(Graphics.COLOR_LT_GRAY, Graphics.COLOR_TRANSPARENT);
        var next = _m.currentExercise().name + " · serie " + _m.currentSetNumber();
        dc.drawText(cx, h * 0.78, Graphics.FONT_TINY, next, Graphics.TEXT_JUSTIFY_CENTER);

        dc.drawText(cx, h * 0.88, Graphics.FONT_TINY, "toca: saltar", Graphics.TEXT_JUSTIFY_CENTER);
    }
}
