// stone:job stone:math.pulse
// stone:function pulse_rs

#[no_mangle]
pub extern "C" fn pulse_rs(x: f64, low: f64, high: f64) -> f64 {
    if low <= x && x <= high { 1.0 } else { 0.0 }
}
