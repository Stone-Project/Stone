// stone:job stone:math.pulse_wave
// stone:function pulse_wave_rs

#[no_mangle]
pub extern "C" fn pulse_wave_rs(x: f64, duty: f64) -> f64 {
    if duty <= 0.0 || duty >= 1.0 { return f64::NAN; }
    if x.rem_euclid(1.0) < duty { 1.0 } else { 0.0 }
}
