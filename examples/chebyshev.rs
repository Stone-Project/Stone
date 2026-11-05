// stone:job stone:math.chebyshev
// stone:function chebyshev_rs

#[no_mangle]
pub extern "C" fn chebyshev_rs(x1: f64, y1: f64, x2: f64, y2: f64) -> f64 {
    (x2 - x1).abs().max((y2 - y1).abs())
}
