// stone:job stone:math.bounce_out
// stone:function bounce_out_rs

#[no_mangle]
pub extern "C" fn bounce_out_rs(t: f64) -> f64 {
    if t < 1.0 / 2.75 {
        7.5625 * t * t
    } else if t < 2.0 / 2.75 {
        let u = t - 1.5 / 2.75;
        7.5625 * u * u + 0.75
    } else if t < 2.5 / 2.75 {
        let u = t - 2.25 / 2.75;
        7.5625 * u * u + 0.9375
    } else {
        let u = t - 2.625 / 2.75;
        7.5625 * u * u + 0.984375
    }
}
