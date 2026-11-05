// stone:job stone:math.saw_wave_safe
// stone:function saw_wave_safe_rs

#[no_mangle]
pub extern "C" fn saw_wave_safe_rs(x: f64) -> f64 {
    if !x.is_finite() { return f64::NAN; }
    x - x.floor()
}
