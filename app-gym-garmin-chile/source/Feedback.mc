import Toybox.Lang;
using Toybox.Attention;
using Toybox.Application;

// ---------------------------------------------------------------------------
// Avisos hápticos y sonoros. Los modelos objetivo (Venu / Venu Sq) NO tienen
// altavoz, así que "que diga sesión completa" se resuelve con vibración + tono
// + la pantalla. Todo va protegido con `has` porque no todos los dispositivos
// exponen las mismas APIs.
// ---------------------------------------------------------------------------
module Feedback {

    function _vibrationEnabled() as Boolean {
        var v = Application.Properties.getValue("vibration");
        return (v == null) ? true : v;
    }

    function _vibe(dutyCycle as Number, lengthMs as Number) as Void {
        if (!_vibrationEnabled()) { return; }
        if (Attention has :vibrate) {
            Attention.vibrate([new Attention.VibeProfile(dutyCycle, lengthMs)]);
        }
    }

    function _tone(tone as Number) as Void {
        if (Attention has :playTone) {
            Attention.playTone(tone);
        }
    }

    // Fin de una serie: una vibración corta + tono suave.
    function setDone() as Void {
        _vibe(50, 250);
        _tone(Attention.TONE_KEY);
    }

    // Fin del descanso: doble vibración para "¡a la siguiente!".
    function restOver() as Void {
        if (_vibrationEnabled() && Attention has :vibrate) {
            Attention.vibrate([
                new Attention.VibeProfile(75, 300),
                new Attention.VibeProfile(0, 150),
                new Attention.VibeProfile(75, 300)
            ]);
        }
        _tone(Attention.TONE_INTERVAL_ALERT);
    }

    // Sesión completa: vibración larga y marcada + tono de éxito.
    function sessionComplete() as Void {
        if (_vibrationEnabled() && Attention has :vibrate) {
            Attention.vibrate([
                new Attention.VibeProfile(100, 500),
                new Attention.VibeProfile(0, 150),
                new Attention.VibeProfile(100, 500),
                new Attention.VibeProfile(0, 150),
                new Attention.VibeProfile(100, 800)
            ]);
        }
        _tone(Attention.TONE_SUCCESS);
    }
}
