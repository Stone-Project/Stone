// stone:job stone:math.remap_safe
// stone:function remap_safe_rs

#[no_mangle]
pub extern "C" fn remap_safe_rs(x: f64, in_min: f64, in_max: f64, out_min: f64, out_max: f64) -> f64 {
    if !(x.is_finite() && in_min.is_finite() && in_max.is_finite() && out_min.is_finite() && out_max.is_finite()) { return f64::NAN; }
    if in_min == in_max { return f64::NAN; }
    out_min + (out_max - out_min) * (x - in_min) / (in_max - in_min)
}
