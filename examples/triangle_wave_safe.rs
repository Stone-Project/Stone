// stone:job stone:math.triangle_wave_safe
// stone:function triangle_wave_safe_rs

#[no_mangle]
pub extern "C" fn triangle_wave_safe_rs(x: f64) -> f64 {
    if !x.is_finite() { return f64::NAN; }
    1.0 - (2.0 * x.rem_euclid(1.0) - 1.0).abs()
}
