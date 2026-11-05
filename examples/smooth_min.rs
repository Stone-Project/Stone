// stone:job stone:math.smooth_min
// stone:function smooth_min_rs

#[no_mangle]
pub extern "C" fn smooth_min_rs(a: f64, b: f64, k: f64) -> f64 {
    if k <= 0.0 { return a.min(b); }
    let h = (k - (a - b).abs()).max(0.0) / k;
    a.min(b) - h * h * k * 0.25
}
