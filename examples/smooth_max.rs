// stone:job stone:math.smooth_max
// stone:function smooth_max_rs

#[no_mangle]
pub extern "C" fn smooth_max_rs(a: f64, b: f64, k: f64) -> f64 {
    if k <= 0.0 { return a.max(b); }
    let h = (k - (a - b).abs()).max(0.0) / k;
    a.max(b) + h * h * k * 0.25
}
