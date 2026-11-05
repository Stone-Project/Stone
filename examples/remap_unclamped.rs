// stone:job stone:math.remap_unclamped
// stone:function remap_unclamped_rs

#[no_mangle]
pub extern "C" fn remap_unclamped_rs(x: f64, in_min: f64, in_max: f64, out_min: f64, out_max: f64) -> f64 {
    if in_min == in_max { return f64::NAN; }
    out_min + (out_max - out_min) * (x - in_min) / (in_max - in_min)
}
