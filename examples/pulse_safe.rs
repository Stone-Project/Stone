// stone:job stone:math.pulse_safe
// stone:function pulse_safe_rs

#[no_mangle]
pub extern "C" fn pulse_safe_rs(x: f64, duty: f64) -> f64 {
    if !(x.is_finite() && duty.is_finite()) { return f64::NAN; }
    if duty <= 0.0 || duty >= 1.0 { return f64::NAN; }
    if x.rem_euclid(1.0) < duty { 1.0 } else { 0.0 }
}
